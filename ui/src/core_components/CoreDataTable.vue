<template>
  <n-config-provider :theme="darkTheme">
    <div
      class="component"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    >
      <n-data-table
        :data="data"
        :columns="columns"
        :bordered="false"
        :max-height="400"
        virtual-scroll
      />
    </div>
  </n-config-provider>
</template>

<script>
import { defineComponent, toRaw } from "vue";
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
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    data: function () {
      let content = this.streamsync.getRawValue(this.componentId, "data");
      return content;
    },
    columns: function () {
      let content = this.streamsync.getRawValue(this.componentId, "columns");
      return content;
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
});
</script>

<style>
</style>
