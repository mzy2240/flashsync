<template>
  <n-config-provider :theme="theme.theme">
    <n-checkbox :label="text" :data-streamsync-id="componentId" v-show="!isPlaceholder">
    </n-checkbox>
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
});
</script>