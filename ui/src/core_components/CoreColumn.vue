<template>
	<div
		class="CoreColumn"
		:style="rootStyle"
		:class="{
			sticky: isSticky,
			collapsible: isCollapsible,
			collapsibleToRight: isCollapsibleToRight,
			collapsed: isCollapsed,
		}"
	>
		<div class="header" v-if="fields.title || isCollapsible">
			<div class="titleContainer" v-if="!isCollapsed">
				<h2 v-if="fields.title">{{ fields.title }}</h2>
			</div>
			<div
				class="collapser"
				v-on:click="toggleCollapsed"
				v-if="isCollapsible"
			>
				<IconGen
					class="collapserArrow"
					icon-key="collapseArrow"
				></IconGen>
			</div>
		</div>
		<div class="collapsedTitle" v-if="isCollapsed && fields.title">
			<div class="transformed">
				<div class="content">{{ fields.title }}</div>
			</div>
		</div>
		<div
			class="container"
			data-streamsync-container
			:style="containerStyle"
		>
			<slot></slot>
		</div>
	</div>
</template>

<script lang="ts">
import { FieldCategory, FieldType } from "../streamsyncTypes";
import { separatorColor } from "../renderer/sharedStyleFields";

const description =
	"A layout component that organises its child components in columns. Must be inside a Column Container component.";

export default {
	streamsync: {
		name: "Column",
		description,
		allowedParentTypes: ["columns", "repeater"],
		allowedChildrenTypes: ["*"],
		category: "Layout",
		fields: {
			title: {
				name: "Title",
				type: FieldType.Text,
			},
			width: {
				name: "Width (factor)",
				default: "1",
				init: "1",
				type: FieldType.Number,
				desc: "Relative size when compared to other columns in the same container. A column of width 2 will be double the width of one with width 1.",
				category: FieldCategory.Style,
			},
			isSticky: {
				name: "Sticky",
				default: "no",
				type: FieldType.Text,
				options: {
					no: "No",
					yes: "Yes",
				},
				category: FieldCategory.Style,
			},
			isCollapsible: {
				name: "Collapsible",
				default: "no",
				type: FieldType.Text,
				options: {
					no: "No",
					yes: "Yes",
				},
				category: FieldCategory.Style,
			},
			startCollapsed: {
				name: "Start collapsed",
				type: FieldType.Text,
				category: FieldCategory.Style,
				default: "no",
				options: {
					yes: "Yes",
					no: "No",
				},
				desc: "Only applied when the column is collapsible.",
			},
			horizontalAlignment: {
				name: "Horizontal alignment",
				default: "normal",
				type: FieldType.Text,
				options: {
					normal: "Normal",
					left: "Left",
					center: "Center",
					right: "Right",
				},
				category: FieldCategory.Style,
			},
			verticalAlignment: {
				name: "Vertical alignment",
				default: "normal",
				type: FieldType.Text,
				options: {
					normal: "Normal",
					left: "Left",
					center: "Center",
					right: "Right",
				},
				category: FieldCategory.Style,
			},
			separatorColor,
		},
	},
	components: { IconGen },
};
</script>
<script setup lang="ts">
import { computed, ComputedRef, inject, Ref, ref, watch } from "vue";
import injectionKeys from "../injectionKeys";
import IconGen from "../renderer/IconGen.vue";
const instancePath = inject(injectionKeys.instancePath);
const instanceData = inject(injectionKeys.instanceData);
const ss = inject(injectionKeys.core);
const componentId = inject(injectionKeys.componentId);

const fields = inject(injectionKeys.evaluatedFields);
const isCollapsible = computed(() => fields.value?.isCollapsible == "yes");
const isCollapsed: Ref<boolean> = ref(
	fields.value?.isCollapsible == "yes" &&
		fields.value?.startCollapsed == "yes"
);
const isSticky = computed(() => fields.value?.isSticky == "yes");

const rootStyle = computed(() => {
	let flex: string;
	if (!isCollapsed.value) {
		flex = `${fields.value.width} 0 0`;
	} else {
		flex = `0 0 32px`;
	}
	const style = {
		flex,
	};
	return style;
});

const containerStyle = computed(() => {
	const horizontalAlignMap = {
		normal: "normal",
		left: "start",
		center: "center",
		right: "end",
	};
	const verticalAlignMap = {
		normal: "normal",
		top: "start",
		center: "center",
		bottom: "end",
	};
	const alignItems = horizontalAlignMap[fields.value.horizontalAlignment];
	const justifyContent = verticalAlignMap[fields.value.verticalAlignment];
	const style = {
		"align-items": alignItems,
		"justify-content": justifyContent,
	};
	return style;
});

const toggleCollapsed = () => {
	isCollapsed.value = !isCollapsed.value;
};

/* Collapsing direction
The minimum non-collapsible column position (mnccp) determines how other columns collapse.
Those with a position lower than mnccp collapse to the left.
Those with a position higher than mnccp collapse to the right.
*/

const isCollapsibleToRight = computed(
	() =>
		position.value >= columnsData.value.value?.minimumNonCollapsiblePosition
);

const columnsData: ComputedRef<Ref> = computed(() => {
	for (let i = -1; i > -1 * instancePath.length; i--) {
		const item = instancePath.at(i);
		const type = ss.getComponentById(item.componentId)?.type;
		if (type !== "columns") continue;
		const columnsData = instanceData.at(i);
		return columnsData;
	}
});

const position = computed(() => ss.getComponentById(componentId)?.position);

watch([() => fields.value?.isCollapsible, position], () => {
	const cd = columnsData.value;
	if (!cd) return;
	cd.value = { minimumNonCollapsiblePosition: undefined };
});

watch(
	columnsData,
	(newColumnsData) => {
		if (!newColumnsData || !newColumnsData.value) return;
		if (isCollapsible.value) return;
		if (
			typeof newColumnsData.value.minimumNonCollapsiblePosition !==
				"undefined" &&
			position.value >= newColumnsData.value.minimumNonCollapsiblePosition
		)
			return;
		newColumnsData.value.minimumNonCollapsiblePosition = position.value;
	},
	{ immediate: true, deep: true }
);
</script>

<style scoped>
@import "../renderer/sharedStyles.css";

.CoreColumn {
	min-width: 0;
	align-self: stretch;
	display: flex;
	flex-direction: column;
	gap: 16px;
}

.CoreColumn.sticky {
	position: sticky;
	top: 16px;
	align-self: flex-start;
}

.CoreColumn > .header {
	display: flex;
	gap: 16px;
	align-items: center;
}

.CoreColumn > .header > .titleContainer {
	flex: 1 0 0;
	order: 1;
}

.CoreColumn.collapsible.collapsibleToRight > .header > .titleContainer {
	order: 3;
	text-align: right;
}

.CoreColumn > .header > .collapser {
	order: 2;
	flex: 0 0 32px;
	border-radius: 16px;
	padding: 4px;
	background: var(--separatorColor);
	display: flex;
	align-items: center;
	justify-content: center;
	stroke: var(--primaryTextColor);
}

.CoreColumn > .header > .collapser > .collapserArrow {
	transition: all 0.5s ease-in-out;
	transform: rotate(0deg);
}

.CoreColumn:not(.collapsibleToRight).collapsed
	> .header
	> .collapser
	> .collapserArrow {
	transform: rotate(180deg);
}

.CoreColumn.collapsibleToRight:not(.collapsed)
	> .header
	> .collapser
	> .collapserArrow {
	transform: rotate(180deg);
}

.CoreColumn.collapsibleToRight > .header {
	justify-content: left;
}

.CoreColumn > .container {
	flex: 1 0 0;
	align-self: stretch;
	width: 100%;
}

.CoreColumn.collapsible.collapsed > .container {
	display: none;
}

.CoreColumn > .collapsedTitle {
	padding-top: 8px;
	opacity: 0.5;
	min-height: 200px;
	overflow: hidden;
}

.CoreColumn > .collapsedTitle > .transformed {
	transform: rotate(90deg);
}

.CoreColumn > .collapsedTitle > .transformed > .content {
	width: 200px;
	color: var(--primaryTextColor);
	white-space: nowrap;
	font-size: 0.9rem;
	text-overflow: ellipsis;
	overflow: hidden;
}

@media only screen and (max-width: 768px) {
	.CoreColumn {
		min-width: 100%;
	}

	.CoreColumn.sticky {
		position: static;
	}
}
</style>
