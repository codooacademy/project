/** @odoo-module **/

import { ProjectControlPanel } from "@project/components/project_control_panel/project_control_panel";
import { patch } from "@web/core/utils/patch";

patch(ProjectControlPanel.prototype, {
    setup() {
        super.setup(...arguments);
    },

    async loadData() {
        super.loadData(...arguments);
        const [data] = await Promise.all([
            this.orm.call("project.project", "get_epic_count", [this.projectId]),
        ]);
        this.epicCount = data.epicCount;
    },

    async onEpicClick(ev) {
        ev.preventDefault();
        this.actionService.doAction("project_implementation.project_epic_action", {
            additionalContext: {
                default_project_id: this.projectId,
                active_id: this.projectId,
            },
        });
    }
});
