<template>
  <n-button :data-streamsync-id="componentId" v-show="!isPlaceholder" text-color="white">
    {{ text }}
  </n-button>
</template>

<script>

export default {
  inject: ["streamsync"],
  props: {
    componentId: String,
  },
  data: function () {
    return {
      text: "",
    };
  },
  created: function () {
    this.text = this.streamsync.getContentValue(this.componentId, "text");
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
};
</script>