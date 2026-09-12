#import "CHAppleBridge.h"
@implementation CHAppleBridge
+ (instancetype)shared { static CHAppleBridge *v; static dispatch_once_t once; dispatch_once(&once, ^{ v=[CHAppleBridge new]; }); return v; }
- (NSDictionary *)applicationMetadata { return @{ @"platform": @"Apple", @"native": @"Objective-C" }; }
- (void)processEvent:(NSDictionary *)event completion:(void (^)(BOOL))completion { dispatch_async(dispatch_get_global_queue(QOS_CLASS_USER_INITIATED,0), ^{ BOOL ok=(event != nil); dispatch_async(dispatch_get_main_queue(), ^{ if(completion) completion(ok); }); }); }
@end
