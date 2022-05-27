
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
import CoreGrid from "./core_components/CoreGrid.vue";
import CoreCard from "./core_components/CoreCard.vue";
import CoreImage from "./core_components/CoreImage.vue";
import CoreInput from "./core_components/CoreInput.vue";
import CoreProgressbar from "./core_components/CoreProgressbar.vue";
import CoreSpin from "./core_components/CoreSpin.vue";
import CoreRichText from "./core_components/CoreRichText.vue";
import CoreMessage from "./core_components/CoreMessage.vue";
import CoreTimePicker from "./core_components/CoreTimePicker.vue";
import CoreDatePicker from "./core_components/CoreDatePicker.vue";
import CorePlotly from "./core_components/CorePlotly.vue";
import CoreDropdown from "./core_components/CoreDropdown.vue";
import CoreCheckbox from "./core_components/CoreCheckbox.vue";
import CoreRadio from "./core_components/CoreRadio.vue";
import CoreTabs from "./core_components/CoreTabs.vue";

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
    "grid": CoreGrid,
    "card": CoreCard,
    "image": CoreImage,
    "input": CoreInput,
    "progressbar": CoreProgressbar,
    "spin": CoreSpin,
    "rich_text": CoreRichText,
    "message": CoreMessage,
    "time_picker": CoreTimePicker,
    "date_picker": CoreDatePicker,
    "plot_plotly": CorePlotly,
    "dropdown": CoreDropdown,
    "checkbox": CoreCheckbox,
    "radio": CoreRadio,
    "tabs": CoreTabs
}