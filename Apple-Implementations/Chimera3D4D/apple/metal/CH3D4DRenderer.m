#import "CH3D4DRenderer.h"
@implementation CH3D4DRenderer
- (instancetype)init { self=[super init]; if(self){ _device=MTLCreateSystemDefaultDevice(); } return self; }
@end
