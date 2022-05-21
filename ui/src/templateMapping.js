
// Maps Streamsync component types to renderable Vue components

import CoreText from "./core_components/CoreText.vue";
import CoreButton from "./core_components/CoreButton.vue";
import CoreSection from "./core_components/CoreSection.vue";
import CoreWhen from "./core_components/CoreWhen.vue";
import CoreSlider from "./core_components/CoreSlider.vue";
import CorePyplot from "./core_components/CorePyplot.vue";
import CoreHeading from "./core_components/CoreHeading.vue";
import CoreMarkdown from "./core_components/CoreMarkdown.vue";
import CoreLatex from "./core_components/CoreLatex.vue";
import CoreSimpleTable from "./core_components/CoreSimpleTable.vue";
import CoreCode from "./core_components/CoreCode.vue";
import CoreDataTable from "./core_components/CoreDataTable.vue";
import Grid from "./core_components/Grid.vue";

export default {
    "button": CoreButton,
    "text": CoreText,
    "section": CoreSection,
    "when": CoreWhen,
    "slider": CoreSlider,
    "pyplot": CorePyplot,
    "heading": CoreHeading,
    "markdown": CoreMarkdown,
    "latex": CoreLatex,
    "simple_table": CoreSimpleTable,
    "code": CoreCode,
    "data_table": CoreDataTable,
    "grid": Grid
}