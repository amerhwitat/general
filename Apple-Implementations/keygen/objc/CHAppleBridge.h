#import <Foundation/Foundation.h>

@interface CHAppleBridge : NSObject
+ (instancetype)shared;
- (NSDictionary *)applicationMetadata;
- (void)processEvent:(NSDictionary *)event completion:(void (^)(BOOL success))completion;
@end
