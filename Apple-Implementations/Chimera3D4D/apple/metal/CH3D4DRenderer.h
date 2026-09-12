#import <Foundation/Foundation.h>
#import <Metal/Metal.h>
@interface CH3D4DRenderer : NSObject
@property(nonatomic,readonly) id<MTLDevice> device;
- (instancetype)init;
@end
