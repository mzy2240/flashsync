<template>
  <n-config-provider :theme="darkTheme">
    <div
      class="component"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    >
      <n-grid :cols="cols" x-gap="12">
        <n-gi v-for="i in cols" :key="i">
          <div v-bind:id="`a${componentId}-${i-1}`"> dgdsfgdsfgdfgsdfgdfsg </div>
        </n-gi>
      </n-grid>
    </div>
  </n-config-provider>
</template>

<script>
import { defineComponent, onBeforeMount, ref } from "vue";
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
  data: function () {
    return {
      cols: 0,
    };
  },
  beforeMount() {
    console.log(this.componentId);
    this.cols = this.streamsync.getRawValue(this.componentId, "cols");
    console.log("cols", this.cols);
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    // cols: function () {
    //   let content = this.streamsync.getRawValue(this.componentId, "cols");
    //   return content;
    // },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
});
</script>

<style>
</style>
