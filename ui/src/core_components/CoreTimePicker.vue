<template>
  <n-config-provider :theme="theme">
    <n-time-picker
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
      :actions="null"
      :minutes="0"
      :seconds="0"
      @update:formatted-value="handleUpdate"
    />
  </n-config-provider>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useThemeStore } from "@/stores/theme";

export default defineComponent({
  inject: ["streamsync"],
  setup() {
    const theme = useThemeStore();
    return {
      theme,
      text: ref("")
    };
  },
  props: {
    componentId: String,
  },
//   data: function () {
//     return {
//       text: "",
//     };
//   },
  //   created: function () {},
  mounted: function () {
    this.text = this.streamsync.getContentValue(this.componentId, "value");
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
  methods: {
    handleUpdate: function (value) {
      //   this.$emit("change", value);
      let event = {};
      event.type = "change";
      event.targetId = this.componentId;
      event.value = value;
      this.streamsync.forward(event, true);
    },
  },
});
</script>