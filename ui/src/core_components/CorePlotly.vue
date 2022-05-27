<template>
  <div
    class="component"
    :data-streamsync-id="componentId"
    v-if="!isPlaceholder"
  >
    <div :id="componentId"></div>
  </div>
</template>

<script>
import Plotly from "plotly.js-dist/plotly";

export default {
  inject: ["streamsync"],
  props: {
    componentId: String,
  },
  created: function () {
    // console.log("markdown created");
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
    const obj = JSON.parse(this.fig);
    Plotly.react(this.componentId, obj.data, obj.layout, obj.config);
  },
  computed: {
    fig: function () {
      let content = this.streamsync.getRawValue(this.componentId, "figure");
      console.log(content)
      return content;
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
};
</script>

<style scope>
</style>
