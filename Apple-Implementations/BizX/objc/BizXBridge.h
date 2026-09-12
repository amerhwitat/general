#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN
@interface BizXBridge : NSObject
+ (instancetype)shared;
- (NSDictionary *)portfolioState;
- (void)publishConversationEvent:(NSDictionary *)event completion:(void (^)(BOOL ok))completion;
@end
NS_ASSUME_NONNULL_END
