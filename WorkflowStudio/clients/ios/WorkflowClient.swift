import Foundation
import AVFoundation

public struct WorkflowProject: Codable { public let id:String; public let name:String; public let methodology:String }
public final class VoiceController: NSObject { private let synthesizer=AVSpeechSynthesizer(); public func speak(_ text:String, language:String="en-US"){let u=AVSpeechUtterance(string:text);u.voice=AVSpeechSynthesisVoice(language:language);synthesizer.speak(u)} }
public final class WorkflowClient { public init(){}; public func healthURL()->URL{return URL(string:"http://localhost:8080/health")!} }
