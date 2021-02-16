class EventChannel(object):
    def __init__(self):
        self.subscribers = {}

    def unsubscribe(self, event, callback):
        if event is not None or event != ""\
                and event in self.subscribers.keys():
            self.subscribers[event] = list(
                filter(
                    lambda x: x is not callback,
                    self.subscribers[event]
                )
            )

    def subscribe(self, event, callback):
        if not callable(callback):
            raise ValueError("callback must be callable")

        if event is None or event == "":
            raise ValueError("Event cant be empty")

        if event not in self.subscribers.keys():
            self.subscribers[event] = [callback]
        else:
            self.subscribers[event].append(callback)

    def publish(self, event, args):
        if event in self.subscribers.keys():
            for callback in self.subscribers[event]:
                callback(args)


if __name__ == "__main__":
    event_channel = EventChannel()

    callback = lambda x: print(x)

    event_channel.subscribe("myevent", callback)

    event_channel.publish("myevent", "Hello, world!")

    # out: "Hello, world!"

    event_channel.unsubscribe("myevent", callback)

    event_channel.publish("myevent", "Hello, world!")

    # No output