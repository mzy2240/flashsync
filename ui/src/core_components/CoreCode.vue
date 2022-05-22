<template>
  <n-config-provider :hljs="hljs">
    <div
      class="component"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    >
      <n-code :code="text" language="python" />
    </div>
  </n-config-provider>
</template>

<script>
import { defineComponent } from "vue";
import { NConfigProvider, NCode } from "naive-ui";
import hljs from "highlight.js/lib/core";
import "highlight.js/styles/github-dark.css";
import python from "highlight.js/lib/languages/python";

hljs.registerLanguage("python", python);

export default defineComponent({
  inject: ["streamsync"],
  components: {
    NConfigProvider,
    NCode,
  },
  setup() {
    return {
      hljs,
    };
  },
  props: {
    componentId: String,
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    text: function () {
      let content = this.streamsync.getContentValue(this.componentId, "text");
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
