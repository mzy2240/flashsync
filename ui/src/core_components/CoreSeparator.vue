<template>
	<div class="CoreSeparator separator">
		<div class="line"></div>
	</div>
</template>

<script lang="ts">
import { separatorColor } from "../renderer/sharedStyleFields";

const description =
	"A visual component to create a separation between adjacent elements.";

const docs = `
_Separator_ components are used to separate layout elements. They can be used in most containers, including _Column Container_ to separate columns.

If the container flows horizontally (like a _Horizontal Stack_ or a _Column Container_) the _Separator_ will be a vertical line. Otherwise, it'll be a horizontal line. 
`;

export default {
	streamsync: {
		name: "Separator",
		description,
		docs,
		category: "Layout",
		fields: {
			separatorColor,
		},
	},
};
</script>

<style scoped>
@import "../renderer/sharedStyles.css";
.CoreSeparator {
	min-height: 1px;
	min-width: 1px;
	align-self: stretch;
	margin: -4px;
	padding: 4px;
}

.line {
	background-color: var(--separatorColor);
	width: 100%;
	height: 100%;
	min-height: 1px;
	min-width: 1px;
}
</style>
