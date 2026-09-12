#import "CH3D4DViewport.h"
#import <QuartzCore/QuartzCore.h>
@implementation CH3D4DViewport
+ (Class)layerClass { return [CAMetalLayer class]; }
- (instancetype)initWithFrame:(NSRect)frame { self=[super initWithFrame:frame]; if(self){ self.wantsLayer=YES; self.layer=[CAMetalLayer layer]; } return self; }
@end
