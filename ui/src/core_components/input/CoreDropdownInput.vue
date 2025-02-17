<template>
	<div class="CoreDropdownInput" ref="rootEl">
		<label class="mainLabel">{{ fields.label }}</label>
		<div class="selectContainer">
			<select
				:value="formValue"
				v-on:input="($event) => handleInput(($event.target as HTMLInputElement).value, 'ss-option-change')"
			>
				<option
					v-for="(option, optionKey) in fields.options"
					:key="optionKey"
					:value="optionKey"
				>
					{{ option }}
				</option>
			</select>
		</div>
	</div>
</template>

<script lang="ts">
import { inject, Ref } from "vue";
import { ref } from "vue";
import { FieldType } from "../../streamsyncTypes";

const description =
	"A user input component that allows users to select a single value from a list of options using a dropdown menu (also known as a select input).";
const defaultOptions = { a: "Option A", b: "Option B" };
const onChangeHandlerStub = `
def onchange_handler(state, payload):

	# Set the state variable "selected" to the selected option

	state["selected"] = payload`;

export default {
	streamsync: {
		name: "Dropdown Input",
		description,
		category: "Input",
		fields: {
			label: {
				name: "Label",
				init: "Input Label",
				type: FieldType.Text,
			},
			options: {
				name: "Options",
				control: "object",
				desc: "Key-value object with options. Must be a JSON string or a state reference to a dictionary.",
				type: FieldType.KeyValue,
				default: JSON.stringify(defaultOptions, null, 2),
			},
		},
		events: {
			"ss-option-change": {
				desc: "Sent when the selected option changes.",
				stub: onChangeHandlerStub.trim(),
				bindable: true,
			},
		},
	},
};
</script>

<script setup lang="ts">
import injectionKeys from "../../injectionKeys";
import { useFormValueBroker } from "../../renderer/useFormValueBroker";

const fields = inject(injectionKeys.evaluatedFields);
const rootEl: Ref<HTMLElement> = ref(null);
const ss = inject(injectionKeys.core);
const componentId = inject(injectionKeys.componentId);

const { formValue, handleInput } = useFormValueBroker(ss, componentId, rootEl);
</script>

<style scoped>
@import "../../renderer/sharedStyles.css";
.CoreSelectInput {
	width: 100%;
}

label {
	color: var(--primaryTextColor);
}

.selectContainer {
	margin-top: 8px;
}
</style>
