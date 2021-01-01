import pynvim

@pynvim.plugin
class TestPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('TestCommand', nargs='*', range='')
    def testcommand(self, args, range):
        self.nvim.current.line = ('Command with args: {}, range: {}'.format(args, range))

    @pynvim.function('TestFunction', sync=True)
    def testfunction(self, args):
        self.nvim.out_write(self.nvim.current.line + "\n")
