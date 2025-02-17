<script lang="ts">
import { computed, h, inject } from "vue";
import { FieldType } from "../streamsyncTypes";
import injectionKeys from "../injectionKeys";

const description =
	"A container component that repeats its child components based on a dictionary.";

const defaultRepeaterObject = {
	a: { desc: "Option A" },
	b: { desc: "Option B" },
};

export default {
	streamsync: {
		name: "Repeater",
		description,
		category: "Other",
		allowedChildrenTypes: ["inherit"],
		fields: {
			repeaterObject: {
				name: "Repeater object",
				default: JSON.stringify(defaultRepeaterObject, null, 2),
				type: FieldType.Object,
				desc: "Include a state reference to the dictionary used for repeating the child components. Alternatively, specify a JSON object.",
			},
			keyVariable: {
				name: "Key variable name",
				default: "itemId",
				init: "itemId",
				type: FieldType.Text,
				desc: "Set the name of the variable that will store the key of the current repeater object entry.",
			},
			valueVariable: {
				name: "Value variable name",
				default: "item",
				init: "item",
				type: FieldType.Text,
				desc: "Set the name of the variable that will store the value of the current repeater object entry.",
			},
		},
	},
	setup(props, { slots }) {
		const ss = inject(injectionKeys.core);
		const componentId = inject(injectionKeys.componentId);
		const fields = inject(injectionKeys.evaluatedFields);
		const renderProxiedComponent = inject(
			injectionKeys.renderProxiedComponent
		);

		const children = computed(() => ss.getComponents(componentId, true));
		const getRepeatedChildrenVNodes = () => {
			if (typeof fields.value.repeaterObject !== "object") {
				return [];
			}

			const repeatedChildrenVNodes = Object.values(
				fields.value.repeaterObject
			).map((item, itemIndex) =>
				children.value.map((childComponent) =>
					renderProxiedComponent(childComponent.id, itemIndex)
				)
			);
			return repeatedChildrenVNodes;
		};

		return () => {
			return h(
				"div",
				{
					class: "CoreRepeater",
					"data-streamsync-container": "",
				},
				children.value.length == 0 ||
					Object.keys(fields.value.repeaterObject).length == 0
					? slots.default({})
					: getRepeatedChildrenVNodes()
			);
		};
	},
};
</script>
<style scoped>
.CoreRepeater:not(.childless) {
	display: contents;
}

[data-streamsync-container].horizontal .CoreRepeater.childless {
	flex: 1 0 auto;
}
</style>
