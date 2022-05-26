<template>
  <n-config-provider :theme="theme.theme">
    <n-date-picker
      type="date"
      :actions="null"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
      @update:formatted-value="updateDate"
    >
    </n-date-picker>
  </n-config-provider>
</template>

<script>
import { useThemeStore } from "@/stores/theme";

export default {
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
  methods: {
    updateDate: function (value) {
      let event = {};
      event.type = "change";
      event.targetId = this.componentId;
      event.value = value;
      this.streamsync.forward(event, true);
    },
  },
};
</script>