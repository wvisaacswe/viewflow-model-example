from viewflow import flow, frontend
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from .models import CheckRequestProcess, TimeOffRequestProcess

@frontend.register
class CheckRequestFlow(Flow):
    process_class = CheckRequestProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["text", "department"]
        ).Permission(
            auto_create=True
        ).Next(this.approve)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.send)
        .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_check
        ).Next(this.end)
    )

    end = flow.End()

    def send_check(self, activation):
        print(activation.process.text)

@frontend.register
class TimeOffRequestFlow(Flow):
    process_class = TimeOffRequestProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["reason", "department"]
        ).Permission(
            auto_create=True
        ).Next(this.approve)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.send)
        .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_request
        ).Next(this.end)
    )

    end = flow.End()

    def send_request(self, activation):
        print(activation.process.text)