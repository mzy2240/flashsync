<template>
  <div
    class="component"
    :data-streamsync-id="componentId"
    v-if="!isPlaceholder"
  >
    <vue-mathjax :formula="text"></vue-mathjax>
  </div>
</template>

<script>
import VueMathjax from "vue-mathjax-next";

export default {
  components: {
    "vue-mathjax": VueMathjax,
  },
  inject: ["streamsync"],
  props: {
    componentId: String,
  },
  data: function () {
    return {
      math: true,
    };
  },
  created: function () {
    this.math = this.streamsync.getRawValue(this.componentId, "math");
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    text: function () {
      let content = this.streamsync.getContentValue(this.componentId, "text");
      if (this.math) {
        content = "$$" + content + "$$";
      }
      return content;
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
};
</script>

<style>
</style>
