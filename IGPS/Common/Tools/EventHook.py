class EventHook:
    
    def __init__(self):
        self.handlers = set()

    def registerForEvent(self, handler):
        self.handlers.add(handler)
        return self

    def deregisterForEvent(self, handler):
        try:
            self.handlers.remove(handler)
        except:
            raise ValueError("Handler is not handling this event, so cannot unhandle it.")
        return self

    def fireEvent(self, *args, **kargs):
        for handler in self.handlers:
            handler(*args, **kargs)

    def getHandlerCount(self):
        return len(self.handlers)
    
    __iadd__ = registerForEvent
    __isub__ = deregisterForEvent
    __call__ = fireEvent
    __len__  = getHandlerCount