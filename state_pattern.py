#!/usr/bin/python3

# 状态模式
# 状态模式关注的事实现一个状态机，状态机的核心部分是状态和状态之间的切换。


from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition


@acts_as_state_machine
class Elevator:
    """
    定义状态机
    状态有：运行，等待，终止，故障
    """
    created = State(initial=True)
    running = State()
    waiting = State()
    terminated = State()
    malfunctioned = State()

    wait = Event(from_states=(created, running, waiting, terminated), to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    terminate = Event(from_states=(running, waiting), to_state=terminated)
    malfunction = Event(from_states=(waiting, running, terminated), to_state=malfunctioned)

    def __init__(self, name):
        # 一个名字
        self.name = name

    @after("wait")
    def wait_info(self):
        print("the {} elevator entered waiting mode".format(self.name))

    @after("run")
    def run_info(self):
        print("the {} elevator is running".format(self.name))

    @before("terminate")
    def terminate_info(self):
        print("the {} elevator terminated".format(self.name))

    @after("malfunction")
    def malfunction_info(self):
        print("the {} elevator malfunctioned".format(self.name))


def transition(elevator, event, event_name):
    try:
        event()
    except InvalidStateTransition as e:
        print("Error: transition of %s from %s to %s failed" % (elevator.name, elevator.current_state, event_name))


def state_info(elevator):
    print("state info %s: %s" % (elevator.name, elevator.current_state))


def main():
    RUNNING = "running"
    WAITING = "waiting"
    TERMINATED = "terminated"
    MALFUNCTIONED = "malfunction"

    e1, e2 = Elevator("first"), Elevator("second")
    [state_info(e) for e in (e1, e2)]

    print()
    transition(e1, e1.wait, WAITING)
    transition(e2, e2.terminate, TERMINATED)
    [state_info(e) for e in (e1, e2)]

    print()
    transition(e1, e1.run, RUNNING)
    transition(e2, e2.wait, WAITING)
    [state_info(e) for e in (e1, e2)]

    print()
    transition(e1, e1.wait, WAITING)
    transition(e2, e2.run, RUNNING)
    [state_info(e) for e in (e1, e2)]

    print()
    [transition(e, e.malfunction, MALFUNCTIONED) for e in (e1, e2)]
    [state_info(e) for e in (e1, e2)]


if __name__ == '__main__':
    main()
