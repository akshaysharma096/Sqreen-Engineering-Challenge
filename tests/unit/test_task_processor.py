from flaskr.utils.task_processing import task_processor


class TestTaskProcessor:
    """
        Unit Tests to test Task Processor Class
    """

    def test_send_to_queue_for_security_event_payload(self, security_event_payload):
        assert task_processor.send_to_queue(security_event_payload) == True

    def test_send_to_queue_for_pulse_event_payload(self, pulse_event_payload):
        assert task_processor.send_to_queue(pulse_event_payload) == True

    def test_send_to_queue_for_playbook_event_payload(self, playbook_event_payload):
        assert task_processor.send_to_queue(playbook_event_payload) == True
