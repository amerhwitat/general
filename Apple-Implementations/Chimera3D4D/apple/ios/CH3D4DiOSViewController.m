#import "CH3D4DiOSViewController.h"
#import <Metal/Metal.h>
#import <QuartzCore/CAMetalLayer.h>

@implementation CH3D4DiOSViewController
- (void)viewDidLoad {
    [super viewDidLoad];
    self.view.backgroundColor = UIColor.blackColor;
    CAMetalLayer *layer = [CAMetalLayer layer];
    layer.device = MTLCreateSystemDefaultDevice();
    layer.frame = self.view.bounds;
    layer.autoresizingMask = kCALayerWidthSizable | kCALayerHeightSizable;
    [self.view.layer addSublayer:layer];
    self.view.multipleTouchEnabled = YES;
}
@end
