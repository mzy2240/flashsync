<template>
  <div
    class="component"
    :data-streamsync-id="componentId"
    v-if="!isPlaceholder"
  >
    <div v-html="html"></div>
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
    // console.log("markdown mounted");
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    text: function () {
      return this.streamsync.getContentValue(this.componentId, "html");
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
};
</script>

<style>
</style>
