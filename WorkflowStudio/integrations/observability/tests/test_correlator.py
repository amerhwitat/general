from WorkflowStudio.integrations.observability.TelemetryCorrelator import correlate
def test_correlation_joins_deployment_and_incident():
    c=correlate({"service_id":"svc","correlation_id":"c1"},{"id":"dep","service_id":"svc"},{"id":"inc"})
    assert c.deployment_id=="dep" and c.incident_id=="inc" and c.correlation_id=="c1"
