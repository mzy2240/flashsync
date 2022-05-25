<template>
  <!-- <n-config-provider :theme="darkTheme"> -->
  <n-spin
    :data-streamsync-id="componentId"
    v-show="!isPlaceholder"
    :show="show"
  >
    <div v-bind:id="`${componentId}`"></div>
  </n-spin>
  <!-- </n-config-provider> -->
</template>

<script>
import { defineComponent } from "vue";
import { darkTheme } from "naive-ui";

export default defineComponent({
  inject: ["streamsync"],
  setup() {
    return {
      darkTheme,
    };
  },
  props: {
    componentId: String,
  },
//   data: function () {
//     return {
//       show: true,
//     };
//   },
//   created() {
//     this.title = this.streamsync.getRawValue(this.componentId, "title");
//   },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    show: function () {
      return this.streamsync.getContentValue(this.componentId, "show");
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
});
</script>

<style>
</style>
