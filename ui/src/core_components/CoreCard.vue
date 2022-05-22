<template>
  <n-config-provider :theme="darkTheme">
    <div
      class="component"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    >
      <n-card :title="title">
        <div v-bind:id="`${componentId}`"></div>
      </n-card>
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
      title: "",
    };
  },
  created() {
    this.title = this.streamsync.getRawValue(this.componentId, "title");
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
