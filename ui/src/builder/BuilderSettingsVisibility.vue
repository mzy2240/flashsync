<template>
	<div class="BuilderSettingsVisibility" v-if="ssbm.isSelectionActive()">
		<div class="sectionTitle">
			<i class="ri-eye-line ri-xl"></i>
			<h3>Visibility</h3>
		</div>
		<div class="main">
			<div class="chipStack">
				<div
					class="chip"
					:class="{
						active:
							typeof component.visible == 'undefined' ||
							component.visible === true,
					}"
					v-on:click="() => setVisibleValue(component.id, true)"
				>
					Yes
				</div>
				<div
					class="chip"
					:class="{ active: component.visible === false }"
					v-on:click="() => setVisibleValue(component.id, false)"
				>
					No
				</div>
				<div
					class="chip"
					:class="{ active: typeof component.visible === 'string' }"
					v-on:click="() => setVisibleValue(component.id, '')"
				>
					Custom
				</div>
			</div>
			<div
				class="fieldWrapper"
				v-if="typeof component.visible === 'string'"
			>
				<span class="name">Visibility value</span>
				<input
					:value="component.visible"
					v-on:input="(ev:Event) => setVisibleValue(component.id, (ev.target as HTMLInputElement).value)"
					type="text"
					class="content"
					placeholder="my_visibility_state_value"
				/>
				<div class="desc">
					Reference a state element that will evaluate to true or
					false. Reference the state element directly, i.e. use
					"my_var" instead of "@{my_var}".
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { computed, inject } from "vue";
import { useComponentActions } from "./useComponentActions";
import injectionKeys from "../injectionKeys";

const ss = inject(injectionKeys.core);
const ssbm = inject(injectionKeys.builderManager);
const { setVisibleValue } = useComponentActions(ss, ssbm);

const component = computed(() => ss.getComponentById(ssbm.getSelectedId()));
</script>

<style scoped>
@import "./sharedStyles.css";

.BuilderSettingsVisibility {
	padding: 24px;
}

.main {
	margin-top: 16px;
}

input {
	padding: 16px 12px 12px 12px;
}
</style>
