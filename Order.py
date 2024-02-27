from Computer import Computer

class Order:

    order_counter = 0

    def __init__(self, computers:list): 
        Order.order_counter =+ 1
        self._id = Order.order_counter
        self._computerList = computers

    @property
    def id(self):
        return id
    
    @property
    def computerList(self):
        computer_str = ''
        for computer in self._computerList:
            computer_str += computer.__str__() + ' | '
        return computer_str
    
    @computerList.setter
    def computerList(self, computers:list): # type: ignore
        self._computerList = computers

    def __str__(self) -> str:
        return f'Order[id:{self._id}, Computers"{self.computerList}]'

    def addComputer(self, computer):
        self._computerList.append(computer)


if __name__ == '__main__':
    from Keyboard import Keyboard
    from Monitor import Monitor
    from Mouse import Mouse

    keyboard1 = Keyboard('Keyboard', 'Logitech')
    # print(keyboard)
    monitor1 = Monitor('Logitech', 'Medium')
    # print(monitor)
    mouse1 = Mouse('Mouse', 'Samsung')
    # print(mouse)
    computer1 = Computer('test-cpu', monitor1, keyboard1, mouse1)

    keyboard2 = Keyboard('Keyboard', 'Logitech')
    # print(keyboard)
    monitor2 = Monitor('Logitech', 'Medium')
    # print(monitor)
    mouse2 = Mouse('Mouse', 'Samsung')
    # print(mouse)
    computer2 = Computer('test-cpu', monitor1, keyboard1, mouse1)

    computers = [computer1, computer2]

    order = Order(computers)

    print(order)

    keyboard3 = Keyboard('Keyboard', 'Logitech')
    # print(keyboard)
    monitor3 = Monitor('Logitech', 'Medium')
    # print(monitor)
    mouse3 = Mouse('Mouse', 'Samsung')
    # print(mouse)
    computer3 = Computer('test-cpu', monitor1, keyboard1, mouse1)

    order.addComputer(computer3)

    print(order)