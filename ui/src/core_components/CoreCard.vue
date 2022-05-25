<template>
  <n-config-provider :theme="darkTheme">
    <div
      class="component"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    >
      <n-card :title="title">
        <div v-for="n in volume" :key="`${n-1}`" v-bind:id="`${componentId}-${n-1}`"></div>
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
      volume: 0
    };
  },
  created() {
    this.title = this.streamsync.getRawValue(this.componentId, "title");
    this.volume = this.streamsync.components[this.componentId].volume;
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
