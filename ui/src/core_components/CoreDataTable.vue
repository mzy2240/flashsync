<template>
  <n-config-provider :theme="theme.theme">
    <div
      class="component"
      :data-streamsync-id="componentId"
      v-if="!isPlaceholder"
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
import { useThemeStore } from "@/stores/theme";

export default defineComponent({
  inject: ["streamsync"],
  setup() {
    const theme = useThemeStore();
    return {
      theme,
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
