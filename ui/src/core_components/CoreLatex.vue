<template>
  <div
    class="component"
    :data-streamsync-id="componentId"
    v-show="!isPlaceholder"
  >
    <div v-html="text"></div>
  </div>
</template>

<script>
import katex from "katex";
import "katex/dist/katex.min.css";

export default {
  inject: ["streamsync"],
  props: {
    componentId: String,
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    text: function () {
      let content = this.streamsync.getContentValue(this.componentId, "text");
      return katex.renderToString(content, {
        throwOnError: false,
        displayMode: true,
        output: "html",
      });
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
};
</script>

<style>
</style>
