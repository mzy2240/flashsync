<template>
  <n-config-provider :theme="darkTheme">
    <div
      class="component"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    >
      <n-grid :cols="cols" x-gap="12">
        <n-gi v-for="i in cols" :key="i">
          <div v-bind:id="`${componentId}-${i - 1}`"></div>
        </n-gi>
      </n-grid>
    </div>
  </n-config-provider>
</template>

<script>
import { defineComponent } from "vue";
import { darkTheme, NConfigProvider, NGrid, NGridItem } from "naive-ui";

export default defineComponent({
  inject: ["streamsync"],
  components: {
    NConfigProvider,
    NGrid,
    NGridItem,
  },
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
  created() {
    this.cols = this.streamsync.getRawValue(this.componentId, "cols");
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
});
</script>

<style>
</style>
