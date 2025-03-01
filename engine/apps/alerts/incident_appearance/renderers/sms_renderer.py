from apps.alerts.incident_appearance.renderers.base_renderer import AlertBaseRenderer, AlertGroupBaseRenderer
from apps.alerts.incident_appearance.renderers.constants import DEFAULT_BACKUP_TITLE
from apps.alerts.incident_appearance.templaters import AlertSmsTemplater
from common.utils import str_or_backup


class AlertSmsRenderer(AlertBaseRenderer):
    @property
    def templater_class(self):
        return AlertSmsTemplater


class AlertGroupSmsRenderer(AlertGroupBaseRenderer):
    @property
    def alert_renderer_class(self):
        return AlertSmsRenderer

    def render(self):
        templated_alert = self.alert_renderer.templated_alert
        title = str_or_backup(templated_alert.title, DEFAULT_BACKUP_TITLE)
        return (
            f"{title}"
        )
