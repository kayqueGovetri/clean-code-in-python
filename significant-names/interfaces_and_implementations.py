# As vezes, há casos especiais para codificações, por exemplo, digamos que voce esteja consatruindo uma ABSTRACT
# FACTORY para criar formas, essa factory será uma interface, e implementada por uma classe concreta. Como devemos
# nomea-la? IShapeFactory e ShapeFactory? É melhor não enfeitar as interfaces, isso gera uma informação adicional
# irrelevante. Não quero que meus usuários saibam que estou lhes dando uma interface, e sim apenas uma ShapeFactory.
# Para codificar a interface é preferivel chama-la de ShapeFactoryImp ou mesmo CShapeFactory
