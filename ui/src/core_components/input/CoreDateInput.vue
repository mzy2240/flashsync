<template>
	<div class="CoreDateInput" ref="rootEl">
		<div class="main">
			<div class="inputContainer">
				<label>{{ fields.label }}</label>
				<input
					type="date"
					v-on:change="($event) => handleInput(($event.target as HTMLInputElement).value, 'ss-date-change')"
				/>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { FieldType } from "../../streamsyncTypes";

const description =
	"A user input component that allows users to select a date using a date picker interface.";

const onChangeHandlerStub = `
def onchange_handler(state, payload):

	# Set the state variable "new_date" to the new value, provided as a YYYY-MM-DD string.

	state["new_date"] = payload`;

export default {
	streamsync: {
		name: "Date Input",
		description,
		category: "Input",
		fields: {
			label: {
				name: "Label",
				init: "Input Label",
				type: FieldType.Text,
			},
		},
		events: {
			"ss-date-change": {
				desc: "Capture changes to this control.",
				stub: onChangeHandlerStub,
				bindable: true,
			},
		},
	},
};
</script>
<script setup lang="ts">
import { inject, Ref, ref } from "vue";
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

.CoreDateInput {
	width: fit-content;
}

label {
	display: block;
	margin-bottom: 8px;
}

input {
	max-width: 20ch;
	width: 100%;
	margin: 0;
	border: 1px solid var(--separatorColor);
}
</style>
