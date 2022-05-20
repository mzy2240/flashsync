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
import { Remarkable } from 'remarkable';

var md = new Remarkable('commonmark');

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
      return md.render(content);
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
};
</script>

<style>
</style>
