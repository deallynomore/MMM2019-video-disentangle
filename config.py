class opt:
    learningRate = 0.002             # learning rate  
    beta1 = 0.9                      # momentum term for adam
    batchSize = 100               # batch size  
    gpu = 2               # gpu to use  
    save = '/media/USERDATA/xrj/MMM2019/exp9'          # base directory to save logs  
    name = 'default'        # checkpoint name
    dataRoot = "/media/DATASET/MMM2019/LASIESTA-move" # data root directory
    dataVal = "/media/DATASET/MMM2019/LASIESTA-move"
    is_mse = True
    optimizer = 'adam'
    eval = True           # optimizer to train with
    nEpochs  = 200              # max training epochs  
    seed      = 1                # random seed  
    epochSize = 50000            # number of samples per epoch  
    contentDim  = 64             # dimensionality of content vector
    poseDim   = 5                # dimensionality of pose vector 
    imageSize = 64               # size of image
    #   dataset   = moving_mnist     # dataset
    movingDigits= 1              # if moving mnist dataset, how many digits to use
    cropSize  = 227              # size of crop (for kitti only)
    maxStep   = 12               # max future time from which to sample future frame from
    nShare    = 1                # number of frame to use for content encoding
    advWeight = 0.0001                # weight on adversarial scene discriminator loss 
    normalize  = True                                 # if set normalize pose and action vectors to have unit norm
    model      = 'dcgan'
    decoder    = 'dcgan'
    depth      = 18              # depth of resnet 
    nThreads   = 0                # number of dataloading threads
    dataPool   = 200
    dataWarmup = 10 
    