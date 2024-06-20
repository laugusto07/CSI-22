# Pizza example using decorators

class PizzaComponent: #Componente
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost
    
class BasicPizza(PizzaComponent): #ConcreteComponent
    cost = 10.0

class ToppingDecorator(PizzaComponent): #Decorator
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
    
    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)

class Cheese(ToppingDecorator): #ConcreteDecoratorA
    cost = 1.0
    def __init__(self, pizzaComponent):
        ToppingDecorator.__init__(self, pizzaComponent)
    
class Bacon(ToppingDecorator): #ConcreteDecoratorB
    cost = 2.0
    def __init__(self, pizzaComponent):
        ToppingDecorator.__init__(self, pizzaComponent)
    
class Ham(ToppingDecorator): #ConcreteDecoratorC
    cost = 1.5
    def __init__(self, pizzaComponent):
        ToppingDecorator.__init__(self, pizzaComponent)
    
class Pepperoni(ToppingDecorator): #ConcreteDecoratorD
    cost = 2.5
    def __init__(self, pizzaComponent):
        ToppingDecorator.__init__(self, pizzaComponent)
    
class Egg(ToppingDecorator): #ConcreteDecoratorE
    cost = 1.5
    def __init__(self, pizzaComponent):
        ToppingDecorator.__init__(self, pizzaComponent)
    
class Mushroom(ToppingDecorator): #ConcreteDecoratorF
    cost = 2.0
    def __init__(self, pizzaComponent):
        ToppingDecorator.__init__(self, pizzaComponent)

class Onions(ToppingDecorator): #ConcreteDecoratorG
    cost = 1.0
    def __init__(self, pizzaComponent):
        ToppingDecorator.__init__(self, pizzaComponent)
    
class Olives(ToppingDecorator): #ConcreteDecoratorH
    cost = 1.5
    def __init__(self, pizzaComponent):
        ToppingDecorator.__init__(self, pizzaComponent)
    
class Pineapple(ToppingDecorator): #ConcreteDecoratorI
    cost = 1.5
    def __init__(self, pizzaComponent):
        ToppingDecorator.__init__(self, pizzaComponent)