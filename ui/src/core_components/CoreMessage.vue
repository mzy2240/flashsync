<template>
  <n-message-provider>
    <div
      class="component"
      :data-streamsync-id="componentId"
      v-if="!isPlaceholder"
    />
  </n-message-provider>
</template>

<script>
import { defineComponent } from "vue";
import iziToast from "izitoast";
import "izitoast/dist/css/iziToast.min.css";

export default defineComponent({
  inject: ["streamsync"],
  props: {
    componentId: String,
  },
  //   data: function () {
  //     return {
  //       message: null,
  //     };
  //   },
  //   created() {
  //     this.message = useMessage();
  //   },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    title: function () {
      return this.streamsync.getContentValue(this.componentId, "title");
    },
    text: function () {
      return this.streamsync.getContentValue(this.componentId, "text");
    },
    duration: function () {
      return this.streamsync.getContentValue(this.componentId, "duration");
    },
    isPlaceholder: function () {
      let signal = this.streamsync.components[this.componentId].placeholder;
      return signal;
    },
  },
  watch: {
    isPlaceholder: function (newVal, oldVal) {
      if (!newVal) {
        iziToast.info({
          title: this.title,
          message: this.text,
          position: "topRight",
          timeout: this.duration,
        });
      }
    },
  },
});
</script>

<style>
.CoreText {
  font-size: 0.8rem;
  white-space: pre-wrap;
}
</style>
