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
  data: function () {
    return {
      data: [],
      columns: [],
    };
  },
  beforeMount() {
    this.data = this.streamsync.getRawValue(this.componentId, "data");
    this.columns = this.streamsync.getRawValue(this.componentId, "columns");
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
