<template>
	<div class="CoreVideoPlayer">
		<video
			:src="fields.src"
			:controls="fields.controls === 'yes'"
			:autoplay="fields.autoplay === 'yes'"
			:loop="fields.loop === 'yes'"
			:muted="fields.muted === 'yes'"
		></video>
	</div>
</template>

<script lang="ts">
import { FieldType } from "../streamsyncTypes";

const description =
	"A video player component that can play various video formats.";

const docs = `
    Use your app's static folder to serve videos directly. For example, \`static/my_video.mp4\`.

Alternatively, you can pack bytes or files in state:

\`state["vid_b"] = ss.pack_bytes(vid_bytes, "video/mp4")\`

\`state["vid_f"] = ss.pack_file(vid_file, "video/mp4")\`

Afterwards, you can reference the video using the syntax \`@{vid_f}\`.

`;

export default {
	streamsync: {
		name: "Video Player",
		description,
		docs,
		category: "Content",
		fields: {
			src: {
				name: "Source",
				desc: "The URL of the video file. Alternatively, you can pass a file via state.",
				default: "",
				type: FieldType.Text,
			},
			controls: {
				name: "Controls",
				desc: "Display video player controls.",
				default: "yes",
				type: FieldType.Text,
				options: {
					yes: "Yes",
					no: "No",
				},
			},
			autoplay: {
				name: "Autoplay",
				desc: "Autoplay the video when the component is loaded.",
				default: "no",
				type: FieldType.Text,
				options: {
					yes: "Yes",
					no: "No",
				},
			},
			loop: {
				name: "Loop",
				desc: "Loop the video when it reaches the end.",
				default: "no",
				type: FieldType.Text,
				options: {
					yes: "Yes",
					no: "No",
				},
			},
			muted: {
				name: "Muted",
				desc: "Mute the video by default.",
				default: "no",
				type: FieldType.Text,
				options: {
					yes: "Yes",
					no: "No",
				},
			},
		},
	},
};
</script>

<script setup lang="ts">
import { inject } from "vue";
import injectionKeys from "../injectionKeys";

const fields = inject(injectionKeys.evaluatedFields);
</script>

<style scoped>
.CoreVideoPlayer {
	width: 100%;
}

video {
	width: 100%;
}
</style>
