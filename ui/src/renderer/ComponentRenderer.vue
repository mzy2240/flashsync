<template>
	<div
		class="ComponentRenderer"
		tabindex="-1"
		:style="rootStyle"
		:class="{ loadingActive: isMessagePending }"
	>
		<RendererNotifications class="notifications"></RendererNotifications>
		<div class="loadingBar"></div>
		<div class="rootComponentArea">
			<ComponentProxy
				v-if="rootComponent"
				:component-id="rootComponent.id"
				:instance-path="rootInstancePath"
				:instance-data="rootInstanceData"
			></ComponentProxy>
			<slot></slot>
		</div>
	</div>
</template>

<script setup lang="ts">
import { inject, ref, Ref, computed, watch } from "vue";
import { Component, InstancePath } from "../streamsyncTypes";
import ComponentProxy from "./ComponentProxy.vue";
import RendererNotifications from "./RendererNotifications.vue";
import injectionKeys from "../injectionKeys";
import { useTemplateEvaluator } from "./useTemplateEvaluator";

const ss = inject(injectionKeys.core);
const templateEvaluator = useTemplateEvaluator(ss);
const pages: Component[] = ss.getComponents();

if (pages.length == 0) {
	console.error("No pages found.");
}

const rootInstancePath: InstancePath = [
	{ componentId: "root", instanceNumber: 0 },
];
const rootInstanceData = [ref(null)];
const rootComponent: Ref<Component> = ref(pages[0]);
const rootFields = computed(() =>
	templateEvaluator.getEvaluatedFields(rootInstancePath)
);
const rootStyle = computed(() => {
	return {
		"--accentColor": rootFields.value.accentColor,
		"--emptinessColor": rootFields.value.emptinessColor,
		"--containerBackgroundColor": rootFields.value.parentIdBackgroundColor,
		"--primaryTextColor": rootFields.value.primaryTextColor,
		"--secondaryTextColor": rootFields.value.secondaryTextColor,
		"--separatorColor": rootFields.value.separatorColor,
	};
});

const isMessagePending = computed(() => ss.isMessagePending.value);

watch(
	() => rootFields.value.appName,
	(appName: string) => {
		updateTitle(appName);
	},
	{ immediate: true }
);

function updateTitle(appName: string) {
	const mode = ss.getMode();
	let title: string;
	if (appName && mode == "edit") {
		title = `${appName} | Streamsync Builder`;
	} else if (!appName && mode == "edit") {
		title = "Streamsync Builder";
	} else if (appName && mode == "run") {
		title = `${appName}`;
	} else if (!appName && mode == "run") {
		title = "Streamsync App";
	}
	document.title = title;
}
</script>

<style scoped>
@import "./sharedStyles.css";

.ComponentRenderer {
	--accentColor: #29cf00;
	--buttonColor: #ffffff;
	--emptinessColor: #e9eef1;
	--separatorColor: rgba(0, 0, 0, 0.07);
	--primaryTextColor: #202829;
	--buttonTextColor: #202829;
	--secondaryTextColor: #5d7275;
	--containerBackgroundColor: #ffffff;
	width: 100%;
	outline: none;
	--notificationsDisplacement: 0;
	font-family: Inter, sans-serif;
	font-size: 0.8rem;
	color: var(--primaryTextColor);
	background: var(--emptinessColor);
	display: flex;
	flex-direction: column;
	min-height: 100%;
	isolation: isolate;
	flex: 1 0 auto;
}
.notifications {
	right: var(--notificationsDisplacement);
}

.loadingBar {
	width: 100%;
	height: 4px;
	margin-bottom: -4px;
	position: sticky;
	top: 0;
	pointer-events: none;
	z-index: 4;
	transition-delay: 0.2s;
	transition-property: opacity;
	transition-duration: 200ms;
	opacity: 0;
}

.loadingActive .loadingBar {
	background-size: 200% 200%;
	opacity: 1;
	animation: loadingAnimation ease-in-out 1s infinite;
	animation-delay: 200ms;
	background-image: linear-gradient(
		270deg,
		var(--emptinessColor),
		var(--accentColor),
		var(--emptinessColor)
	);
}

@keyframes loadingAnimation {
	0% {
		background-position: 0% 0%;
	}
	50% {
		background-position: 100% 100%;
	}
	100% {
		background-position: 0% 0%;
	}
}
.rootComponentArea {
	display: flex;
	flex: 1 0 auto;
}
</style>
