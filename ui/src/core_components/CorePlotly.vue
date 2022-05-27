<template>
  <div
    class="component"
    :data-streamsync-id="componentId"
    v-if="!isPlaceholder"
  >
    <div v-html="text"></div>
  </div>
</template>

<script>
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
  },
  computed: {
    text: function () {
      let content = this.streamsync.getRawValue(this.componentId, "figure");
      console.log(content);
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
