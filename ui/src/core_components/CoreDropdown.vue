<template>
  <n-config-provider :theme="theme.theme">
    <n-space vertical v-show="!isPlaceholder">
      <n-select
        v-model="value"
        :options="options"
        :placeholder="placeholder"
        :data-streamsync-id="componentId"
      />
    </n-space>
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
      value: ref(null),
      theme,
    };
  },
  props: {
    componentId: String,
  },
  data: function () {
    return {
      opts: [],
      placeholder: "",
    };
  },
  created: function () {
    this.placeholder = this.streamsync.getContentValue(
      this.componentId,
      "placeholder"
    );
    this.opts = this.streamsync.getContentValue(this.componentId, "options");
    this.opts = this.opts.map((item) => ({ label: item, value: item }));
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