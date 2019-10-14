from models import *

class BaseModel():
    @classmethod
    def create(cls, message_type = 'resnet'):
        MESSAGE_TYPE_TO_CLASS_MAP = {
            'resnet':  resnet.ResNet18,
            # 'densenet': densenet.DenseNet,
            'densenet': densenetBC.Network,
            #'pyramidnet': pyramidnet.Network,
            'resnet_basic': resnet.ResNet101,
            #'resnext': resnext.Network,
            #'pnasnet': pnasnet.PNASNetB,
            #'vgg' : vgg.VGG,
            #'vgg_bearpaw' : vgg_bearpaw.vgg16_bn,
            #'shake' : shake_resnet.ShakeResNet,
        }

        if message_type not in MESSAGE_TYPE_TO_CLASS_MAP:
            raise ValueError('Bad message type {}'.format(message_type))

        if message_type == 'vgg':
            return MESSAGE_TYPE_TO_CLASS_MAP[message_type]('VGG19')

        return MESSAGE_TYPE_TO_CLASS_MAP[message_type]()
