<template>
  <n-progress
    type="line"
    :percentage="value"
    :indicator-placement="'inside'"
    :data-streamsync-id="componentId"
    v-show="!isPlaceholder"
  />
</template>

<script>
export default {
  inject: ["streamsync"],
  props: {
    componentId: String,
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    value: function () {
      const figure = this.streamsync.getContentValue(
        this.componentId,
        "value"
      );
      return figure;
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
};
</script>

<style>
</style>
